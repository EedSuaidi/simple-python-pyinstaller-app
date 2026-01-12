pipeline {
    agent any

    environment {
        // Token yang udah lo simpen di Credential Jenkins
        VERCEL_TOKEN = credentials('vercel-token')
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Build & Test') {
            steps {
                script {
                    // Test pake image Python
                    docker.image('python:3.9-alpine').inside('-v jenkins-data:/var/jenkins_home:rw -u 0') {
                        dir('sources') {
                            // Install library test manual
                            sh 'pip install pytest'
                            sh 'python -m pytest'
                        }
                    }
                }
            }
        }

        stage('Manual Approval') { // Kriteria 4
            steps {
                script {
                    // Pipeline bakal PAUSE di sini nunggu lo klik
                    input message: 'Lanjutkan ke tahap Deploy?', ok: 'Proceed'
                }
            }
        }

        stage('Deploy to Vercel') { // Kriteria 2 & Saran 3
            steps {
                script {
                    echo 'Deploying to Vercel...'
                    // Pake image Node buat jalanin Vercel CLI
                    docker.image('node:alpine').inside('-u 0') {
                        // Install Vercel CLI
                        sh 'npm install -g vercel'
                        
                        // Deploy command:
                        // --prod: Deploy ke production
                        // --token: Pake token dari credential Jenkins
                        // --yes: Skip konfirmasi
                        // --name: Nama project biar rapi
                        sh 'vercel --prod --token $VERCEL_TOKEN --yes --name submission-cicd-eed'
                    }
                }
            }
        }
        
        stage('Post-Deploy Delay') { // Kriteria 3
            steps {
                echo 'Aplikasi sukses deploy. Menunggu 1 menit agar stabil...'
                sleep 60
            }
        }
    }
    
    post {
        success {
            echo 'Pipeline Selesai! Aplikasi aman sentosa.'
        }
    }
}
