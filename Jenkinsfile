pipeline {
    agent any

    environment {
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
                    docker.image('python:3.9-alpine').inside('-v jenkins-data:/var/jenkins_home:rw -u 0') {
                        dir('sources') {
                            sh 'pip install pytest'
                            sh 'python -m pytest'
                        }
                    }
                }
            }
        }

        stage('Manual Approval') { 
            steps {
                script {
                    input message: 'Lanjutkan ke tahap Deploy?', ok: 'Proceed'
                }
            }
        }

        // REVISI: Sleep masuk sini
        stage('Deploy to Vercel') { 
            steps {
                script {
                    echo 'Deploying to Vercel...'
                    docker.image('node:alpine').inside('-u 0') {
                        sh 'npm install -g vercel'
                        sh 'vercel --prod --token $VERCEL_TOKEN --yes --name submission-cicd-eed'
                    }
                    
                    echo 'Deploy sukses. Menunggu 1 menit (Requirement Reviewer)...'
                    sleep 60 
                }
            }
        }
        
        // Stage 'Post-Deploy Delay' HAPUS
    }
    
    post {
        success {
            echo 'Pipeline Selesai!'
        }
    }
}
