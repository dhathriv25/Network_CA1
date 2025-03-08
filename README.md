# Automated Flask Application Deployment

This project demonstrates an automated deployment pipeline for a containerized Flask application using AWS CloudFormation, Ansible, Docker, and GitHub Actions. The implementation provides a complete end-to-end automation solution from infrastructure provisioning to continuous deployment.

## Project Overview

The goal of this project is to automate the deployment of a server running a containerized web application. The implementation follows DevOps best practices by using Infrastructure as Code (IaC) techniques, configuration management, containerization, and continuous integration/continuous deployment (CI/CD).

The architecture includes:

1. AWS EC2 instance provisioned through CloudFormation
2. Server configuration managed by Ansible
3. Application containerized with Docker
4. Continuous deployment through GitHub Actions

## Components

### Infrastructure as Code

The project uses AWS CloudFormation to provision the cloud infrastructure. The CloudFormation template creates an EC2 instance with the necessary security groups to allow web and SSH traffic. This approach ensures that the infrastructure is reproducible and can be version-controlled.

### Configuration Management

Ansible handles the server configuration after provisioning. The Ansible playbooks install and configure Docker on the EC2 instance, ensuring that Docker starts automatically when the server boots up. This ensures consistent server configuration and reduces manual setup.

### Containerization

The Flask application is containerized using Docker. The Dockerfile specifies the environment, dependencies, and runtime configuration for the application. Containerization provides isolation, consistency across environments, and simplified deployment.

### Continuous Integration/Continuous Deployment

GitHub Actions automates the deployment process. When changes are pushed to the main branch, the GitHub Actions workflow:
1. Connects to the EC2 instance
2. Transfers the updated application files
3. Rebuilds the Docker image
4. Redeploys the container

This automation ensures that the latest version of the application is always deployed with minimal manual intervention.

## Setup Instructions

### Prerequisites

To use this project, you need:
- An AWS account with appropriate permissions
- A GitHub account
- Basic familiarity with AWS, Docker, Ansible and GitHub Actions
- Python 3.8+ for local development

**Important**: You must install Python 3.8 on your EC2 instance before running the deployment workflow. The Ansible playbook specifically looks for Python 3.8 and will fail if it's not available.

To install Python 3.8 on your EC2 instance:

1. Connect to your EC2 instance via SSH: OR You can directly access it from your EC2 page from AWS Console(Recommended)
   ```
   ssh -i your-key.pem ec2-user@your-instance-ip
   ```

2. For Amazon Linux 2, install Python 3.8 using amazon-linux-extras:
   ```
   sudo amazon-linux-extras install python3.8
   ```

3. Alternatively, if the above method doesn't work, install Python 3.8 from source:
   ```
   # Update packages
   sudo yum update -y
   
   # Install development tools
   sudo yum groupinstall "Development Tools" -y
   sudo yum install openssl-devel bzip2-devel libffi-devel -y
   
   # Download and compile Python 3.8
   cd /opt
   sudo wget https://www.python.org/ftp/python/3.8.12/Python-3.8.12.tgz
   sudo tar xzf Python-3.8.12.tgz
   cd Python-3.8.12
   sudo ./configure --enable-optimizations
   sudo make altinstall
   
   # Create a symbolic link
   sudo ln -s /usr/local/bin/python3.8 /usr/bin/python3.8
   ```

4. Verify the installation:
   ```
   python3.8 --version
   which python3.8
   ```

This step is crucial because the deployment playbook specifically checks for Python 3.8 with the command `which python3.8` and will fail if it cannot find it.

### AWS Setup

1. Create an EC2 key pair named "Security-key" in your AWS account
2. Create an IAM role named "EC2-CloudFormation-Role" with the necessary permissions
3. Deploy the CloudFormation stack using the template in the repository
4. Obtain an Elastic IP and associate it to the EC2 instance

### GitHub Setup

1. Fork or clone this repository
2. Add the following secrets to your GitHub repository:
   - AWS_ACCESS_KEY_ID: Your AWS access key
   - AWS_SECRET_ACCESS_KEY: Your AWS secret key
   - EC2_PUBLIC_IP: Public IP of your deployed EC2 instance or associated Elastic IP
   - SSH_PRIVATE_KEY: Private key for SSH access to the EC2 instance

### Local Development

For local development and testing of the Flask application:

1. Clone the repository
2. Navigate to the flask-app directory
3. Install dependencies:
   ```
   pip install -r requirements.txt
   ```
4. Run the application:
   ```
   python app.py
   ```

## Project Structure

```
├── cloudformationsetup.json    # AWS CloudFormation template
├── ConfigDocker.yml            # Ansible playbook for Docker setup
├── flask-app/                  # Flask application
│   ├── app.py                  # Main application file
│   ├── Dockerfile              # Container definition
│   ├── requirements.txt        # Python dependencies
│   ├── deploy_flask.yml        # Ansible deployment playbook
│   └── templates/              # HTML templates
│       └── index.html          # Main page template
├── .github/workflows/          # GitHub Actions workflows
│   ├── deploy.yml              # Deployment workflow
└── README.md                   # This file
```

## Flask Application

The application is a simple Flask web server that serves a static HTML page. The application:
1. Imports Flask and render_template
2. Creates a Flask application instance
3. Defines a route for the home page
4. Renders the index.html template
5. Runs the server on port 80

## Deployment Process

The deployment process follows these steps:

1. Infrastructure Provisioning:
   - CloudFormation creates an EC2 instance with security groups
   - The instance is configured with a public IP address

2. Server Configuration:
   - Ansible installs and configures Docker on the EC2 instance
   - System packages are updated and Docker is set to start on boot

3. Application Deployment:
   - The Flask application files are copied to the server
   - A Docker image is built from the Dockerfile
   - The container is started and mapped to port 80

4. Continuous Deployment:
   - GitHub Actions workflow monitors the repository for changes
   - When changes are detected, the workflow connects to the EC2 instance
   - The application is redeployed automatically

## Troubleshooting

Common issues and solutions:

- Docker Container Not Starting: Check Docker logs with `docker logs my-flask-app`.
- Website Not Accessible: Verify that port 80 is open in the security group.
- GitHub Actions Failures: Check the workflow logs for detailed error messages.

## Future Improvements

Potential improvements for the project:

- Implementing HTTPS with SSL certificates
- Adding monitoring and alerting
- Setting up load balancing for high availability
- Implementing blue-green deployment for zero-downtime updates
- Adding automated testing before deployment

## License

This project is provided for educational purposes and has no licensing you are free to clone it :)
If this helped you in anyway then you can connect with me on LinkedIn: www.linkedin.com/in/dhathriv25

## Acknowledgments

This project was completed as part of the Network Systems and Administration module (B9IS121).
