pipeline {
    agent any

    environment {
        // SonarQube environment defined in Jenkins -> Configure System
        SONARQUBE_ENV = 'My SonarQube Server'
        PATH = "/usr/bin:${env.PATH}"  // Python & sonar-scanner path
    }

    stages {
        stage('Clone') {
            steps {
                git branch: 'main', url: 'https://github.com/ERAPARH/Jenkins-sonar-practice.git'
            }
        }

        stage('Install Dependencies') {
            steps {
                sh 'which python3'
                sh 'python3 --version'
                sh 'pip3 install -r requirements.txt || true'
            }
        }

        stage('Run Tests') {
            steps {
                sh 'python3 -m unittest discover -s .'
            }
        }

        stage('SonarQube Analysis') {
            steps {
                withSonarQubeEnv("${env.SONARQUBE_ENV}") {
                    sh 'sonar-scanner'
                }
            }
        }
    }
}

