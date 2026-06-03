pipeline {
agent any

```
environment {
    IMAGE_NAME = "farm-inventory:v1"
    CONTAINER_NAME = "farm-test"
}

stages {

    stage('Checkout SCM') {
        steps {
            checkout scm
        }
    }

    stage('Build Docker Image') {
        steps {
            sh '''
            docker build \
                -t ${IMAGE_NAME} \
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

    stage('Run Container') {
        steps {
            sh '''
            docker rm -f ${CONTAINER_NAME} || true

            docker run -d \
                --name ${CONTAINER_NAME} \
                -p 8001:8000 \
                ${IMAGE_NAME}
            '''
        }
    }

    stage('Container Debug') {
        steps {
            sh '''
            docker ps -a
            docker logs ${CONTAINER_NAME}
            '''
        }
    }

    stage('Health Check') {
        steps {
            sh '''
            sleep 5

            docker exec ${CONTAINER_NAME} python -c "
```

import urllib.request
response = urllib.request.urlopen('http://localhost:8000/')
print(response.read().decode())
"
'''
}
}
}

```
post {

    always {
        sh '''
        docker rm -f ${CONTAINER_NAME} || true
        '''
    }

    success {
        echo 'Pipeline completed successfully'
    }

    failure {
        echo 'Pipeline failed'
    }
}
```

}
