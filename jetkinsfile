pipeline {
    agent any

    stages {
        stage('Clone Repository') {
            steps {
                git 'https://github.com/MananBagadi100/alpha-mantis.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t flask-app .'
            }
        }

        stage('Run Docker Container') {
            steps {
                sh 'docker run -d -p 5001:5000 --name flask-container flask-app'
            }
        }

        stage('Test API') {
            steps {
                sh 'curl http://localhost:5001/v3/status > build_log.txt'
            }
        }

        stage('Clean Up Docker') {
            steps {
                sh 'docker stop flask-container || true'
                sh 'docker rm flask-container || true'
                sh 'docker rmi flask-app || true'
            }
        }
    }
}
