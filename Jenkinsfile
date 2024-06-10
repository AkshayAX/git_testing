pipeline {
    agent any
    
    parameters {
        string(name:"input",defaultValue:"World",description:"Simple entry level script")
    }

    environment {
        AWS_ACCESS_KEY_ID = credentials('aws-access-key-id')
        AWS_SECRET_ACCESS_KEY = credentials('aws-secret-access-key')
    }

    stages {
        stage("Greet")
        {
            steps {
                echo "Hello ${params.input}, how are you"
            }
        }

        stage("Checkout")
        {
            steps {
                checkout scmGit(branches: [[name: '*/main']], extensions: [], userRemoteConfigs: [[url: 'https://github.com/AkshayAX/git_testing.git']])
            }
        }

        stage("Setup Python") {

            steps {
                sh 'python3 -m pip install --upgrade pip'
            }
        }

        stage("Install Dependencies") {
            steps {
                sh 'pip install -r requirements.txt'
            }
        }

        stage("Run script") {
            steps {
                sh 'python main.py'
                echo "Script executed successfully"
            }
        }

        stage("Run Tests") {
            steps {
                sh 'pytest'
            }
        }

        stage("Create zip file") {

            steps {
                sh 'zip -r artifacts.zip main.py'
            }
        }

        stage("Arhive artifacts") {
            
            steps {
                archiveArtifacts artifacts: 'artifacts.zip', fingerprint: true, followSymlinks: false
            }
        }

        stage("Upload to s3") {
            
            steps {
                withAWS(region: 'ap-south-1', credentials: 'aws-credentials') {
                    s3Upload(file: 'artifacts.zip', bucket: 'axsubucket', path: 'artifacts.zip')
                }
            }
        }
    }
}
