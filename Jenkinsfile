pipeline {
    agent any

    stages {

        stage('Debug') {
            steps {
                sh '''
                pwd
                ls -la
                '''
            }
        }

        stage('Build Docker Image') {
            steps {
                sh '''
                docker build \
                  -t farm-inventory:v1 \
                  -f docker/Dockerfile .
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
