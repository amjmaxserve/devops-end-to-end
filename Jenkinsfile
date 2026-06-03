pipeline {
    agent any

    stages {

        stage('Build Docker Image') {
            steps {
                sh '''
                docker build \
                  -t farm-inventory:v1 \
                  -f docker/Dockerfile .
                '''
            }
        }

        stage('Run Container') {
            steps {
                sh '''
                docker rm -f farm-test || true

                docker run -d \
                  --name farm-test \
                  -p 8001:8000 \
                  farm-inventory:v1
                '''
            }
        }

        stage('Health Check') {
            steps {
                sh '''
                sleep 10

                curl http://localhost:8001/
                '''
            }
        }

        stage('Cleanup') {
            steps {
                sh '''
                docker rm -f farm-test || true
                '''
            }
        }
    }
}
