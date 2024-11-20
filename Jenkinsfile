pipeline {
    agent any

    environment {
        ALLURE_VERSION = '2.21.0'
    }

    stages {
        stage('Setup Environment') {
            steps {
                script {
                    sh '''
                    sudo apt update
                    sudo apt install -y openjdk-11-jdk
                    wget -qO- https://github.com/allure-framework/allure2/releases/download/${ALLURE_VERSION}/allure-${ALLURE_VERSION}.tgz | sudo tar -xz -C /opt/
                    sudo ln -sf /opt/allure-${ALLURE_VERSION}/bin/allure /usr/local/bin/allure
                    '''
                }
            }
        }

        stage('Install Dependencies') {
            steps {
                script {
                    sh 'pip install -r requirements.txt'
                }
            }
        }

        stage('Run Tests') {
            steps {
                script {
                    sh 'pytest --alluredir=reports tests/test_chrome_flow.py'
                }
            }
        }

        stage('Generate Allure Report') {
            steps {
                script {
                    sh 'allure serve reports'
                }
            }
        }

        stage('Publish Allure Report') {
            steps {
                allure([
                    results: [[path: 'reports']],
                    reportBuildPolicy: 'ALWAYS',
                ])
            }
        }
    }
}