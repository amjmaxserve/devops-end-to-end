pipeline {
    agent any

    stages {

        stage('Checkout') {
            steps {
                echo 'Source Code Available'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh '''
                docker build \
                -t farm-inventory:v1 \
                -f Dockerfiles/Dockerfile .
                '''
            }
        }

        stage('Verify Image') {
            steps {
                sh '''
                docker images | grep farm-inventory
                '''
            }
        }
    }
}
