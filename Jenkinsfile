node {
    def pythonImage = 'python:3.9-alpine'

    stage('Checkout') {
        checkout scm
    }

    stage('Build & Test') {
        // Mount volume & User Root (Ini udah bener, pertahankan)
        docker.image(pythonImage).inside('-v jenkins-data:/var/jenkins_home:rw -u 0') {
            
            // FIX: Masuk ke folder 'sources' dulu!
            dir('sources') {
                echo '--- Posisi Sekarang ---'
                sh 'pwd' // Cek folder aktif
                sh 'ls -la' // Pastikan requirements.txt ada di sini
                
                echo '--- Install Dependencies ---'
                // Sekarang requirements.txt pasti ketemu
                sh 'pip install -r requirements.txt'
                
                echo '--- Jalankan Test ---'
                // pytest juga jalanin dari sini karena test file-nya ada di sini
                sh 'python -m pytest'
            }
        }
    }
}
