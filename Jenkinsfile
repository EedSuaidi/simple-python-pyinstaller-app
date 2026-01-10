node {
    def pythonImage = 'python:3.9-alpine'

    stage('Checkout') {
        checkout scm
    }

    stage('Build & Test') {
        // PERBAIKAN:
        // 1. '-v jenkins-data:/var/jenkins_home:rw' -> Maksa container Python baca volume jenkins
        // 2. '-u 0' -> Jalan sebagai Root biar gak error permission pas pip install
        docker.image(pythonImage).inside('-v jenkins-data:/var/jenkins_home:rw -u 0') {
            
            echo '--- Debugging: Cek File ---'
            sh 'ls -la' // Kita cek, filenya beneran nongol gak
            
            echo '--- Cek Python ---'
            sh 'python --version'
            
            echo '--- Install Dependencies ---'
            sh 'pip install -r requirements.txt'
            
            echo '--- Jalankan Test ---'
            sh 'python -m pytest'
        }
    }
}
