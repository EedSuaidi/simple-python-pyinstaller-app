node {
    def pythonImage = 'python:3.9-alpine'

    stage('Checkout') {
        checkout scm
    }

    stage('Build & Test') {
        // Mount volume & User Root (Wajib)
        docker.image(pythonImage).inside('-v jenkins-data:/var/jenkins_home:rw -u 0') {
            
            // Masuk ke folder sources
            dir('sources') {
                echo '--- Cek Lokasi ---'
                sh 'ls -la' 
                
                echo '--- Install Library Test ---'
                // REVISI: Install pytest manual, jangan cari requirements.txt yg ga ada
                sh 'pip install pytest'
                
                echo '--- Jalankan Test ---'
                // Jalanin test pake pytest
                sh 'python -m pytest'
            }
        }
    }
}
