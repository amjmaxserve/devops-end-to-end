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

        stage('Trivy Security Scan') {
            steps {
                sh '''
                docker run --rm \
                -v /var/run/docker.sock:/var/run/docker.sock \
                aquasec/trivy image farm-inventory:v1
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

        stage('Container Debug') {
            steps {
                sh '''
                docker ps -a
                docker logs farm-test || true
                '''
            }
        }
        
	    stage('Health Check') {
            steps {
                sh '''
                sleep 10

                curl http://192.168.29.5:8001/
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

