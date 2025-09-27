pipeline {
    agent any

    environment {
        SONARQUBE_ENV = 'My SonarQube Server'  // Jenkins me configured SonarQube server ka naam
        SONAR_TOKEN = credentials('sonar-token2') // Jenkins credentials me token ka ID
        PATH = "/usr/bin:/opt/sonar-scanner/bin:${env.PATH}"
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
                    sh "sonar-scanner -Dsonar.projectKey=sonar-token2 -Dsonar.sources=. -Dsonar.login=${SONAR_TOKEN}"

                        
                }
            }
        }
    }
}

