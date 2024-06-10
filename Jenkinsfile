pipeline {
    agent any
    
    parameters {
        string(name: "input", defaultValue: "World", description: "Simple entry level script")
    }

    environment {
        AWS_ACCESS_KEY_ID = 'no man'
        AWS_SECRET_ACCESS_KEY = 'no land'
        VENV_DIR = 'venv'
    }

    stages {
        stage("Greet") {
            steps {
                echo "Hello ${params.input}, how are you"
            }
        }

        stage("Checkout") {
            steps {
                git branch: 'main', url: 'https://github.com/AkshayAX/git_testing.git'
            }
        }

        stage("Setup Python") {
            steps {
                sh '''
                    python3 -m venv $VENV_DIR
                    . $VENV_DIR/bin/activate
                    python -m pip install --upgrade pip
                '''
            }
        }

        stage("Install Dependencies") {
            steps {
                sh '''
                    . $VENV_DIR/bin/activate
                    pip install -r requirements.txt
                '''
            }
        }

        stage("Run script") {
            steps {
                sh '''
                    . $VENV_DIR/bin/activate
                    python main.py
                    echo "Script executed successfully"
                '''
            }
        }

        stage("Run Tests") {
            steps {
                sh '''
                    . $VENV_DIR/bin/activate
                    pytest
                '''
            }
        }

        stage("Create zip file") {
            steps {
                sh 'zip -r artifacts.zip main.py'
            }
        }

        stage("Archive artifacts") {
            steps {
                archiveArtifacts artifacts: 'artifacts.zip', fingerprint: true, followSymlinks: false
            }
        }

        stage("Upload to s3") {
            steps {
                withAWS(region: 'ap-south-1', credentials: 'aws-access-key-id') {
                    s3Upload(file: 'artifacts.zip', bucket: 'axsubucket', path: 'artifacts.zip')
                }
            }
    }
}
}
