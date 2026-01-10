node {
    def pythonImage = 'python:3.9-alpine'

    stage('Checkout') {
        checkout scm
    }

    stage('Build & Test') {
        docker.image(pythonImage).inside {
            sh 'python --version'
            // Install dependencies
            sh 'pip install -r requirements.txt'
            // Jalanin test sederhana
            sh 'python -m pytest' 
        }
    }
}
