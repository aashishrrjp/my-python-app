Guide: Deploying a Python Application with a Full GitOps Workflow
This guide provides all the necessary code and configuration to take a simple Python application, containerize it, package it with Helm, and deploy it to Kubernetes using Argo CD.

Core Concepts
Git Repository (Your Repo): The single source of truth for our application's desired state. All changes to the application or its configuration start here.

Docker Image: A portable, self-contained package of our Python application. We'll build this once and reference it in our configurations.

Helm Chart: A package manager for Kubernetes. It allows us to define our application as a configurable, version-controlled chart.

Argo CD: The GitOps tool that automatically syncs the state of our application in the Kubernetes cluster with the configuration defined in our Git repository.

Directory Structure
To get started, create the following directory structure in your Git repository. The files below will be provided in the subsequent code blocks.

/
├── helm/
│   ├── my-python-app/
│   │   ├── Chart.yaml
│   │   ├── values.yaml
│   │   └── templates/
│   │       ├── _helpers.tpl
│   │       ├── deployment.yaml
│   │       └── service.yaml
├── argocd/
│   └── application.yaml
├── app/
│   ├── app.py
│   └── Dockerfile
└── README.md         (This file)

Step 1: Build and Push Your Docker Image
Before you can deploy anything, you need to build the Python application's Docker image and push it to a container registry that your Kubernetes cluster can access (like Docker Hub, Google Container Registry, etc.).

Navigate to the app directory:

cd app

Build the Docker image: Replace your-dockerhub-username with your actual username.

docker build -t your-dockerhub-username/my-python-app:1.0.0 .

Push the image to the registry:

docker push your-dockerhub-username/my-python-app:1.0.0

Note: You may need to run docker login first.

Step 2: Customize Your Helm Chart
The Helm chart defines how your application runs in Kubernetes. The most important file for you to edit is helm/my-python-app/values.yaml.

Open helm/my-python-app/values.yaml.

Change the repository and tag to match the image you just pushed.

image:
  repository: your-dockerhub-username/my-python-app # <-- CHANGE THIS
  tag: "1.0.0"                                    # <-- AND THIS

Step 3: Push Everything to Your Git Repository
Now that your files are ready, commit and push them to your GitHub, GitLab, or other Git provider.

git add .
git commit -m "Initial commit of Python application and Helm chart"
git push

Step 4: Deploy Using Argo CD
This is the final step. We will tell Argo CD to watch our repository and deploy our application.

Customize the Argo CD Manifest: Open argocd/application.yaml and change the repoURL to point to your Git repository.

spec:
  source:
    repoURL: https://github.com/your-username/your-repo-name.git # <-- CHANGE THIS

Apply the Argo CD manifest to your cluster: Make sure you have kubectl configured to point to the Kubernetes cluster where Argo CD is running.

kubectl apply -f argocd/application.yaml

Check Argo CD UI: Open the Argo CD web interface. You should see a new application called my-python-app. Initially, it might be OutOfSync. Click the Sync button to deploy your application for the first time. Once synced, it will turn green and Healthy.

Step 5: Verify Your Application
Once Argo CD shows the application is synced and healthy, you can verify it's running.

# Get the name of your service
kubectl get service my-python-app

# Use port-forwarding to access it on your local machine
kubectl port-forward svc/my-python-app 8080:80

# Now, open your browser or use curl
# You should see the message from your Python app!
curl http://localhost:8080

The GitOps Magic: Making an Update
Want to change the welcome message?

Edit app/app.py.

Re-build and push a new Docker image with a new tag (e.g., 1.0.1).

Update the image.tag in helm/my-python-app/values.yaml to "1.0.1".

Commit and push the change to Git.

Watch Argo CD automatically detect the change and update your deployment in the cluster. You don't need to use kubectl again!