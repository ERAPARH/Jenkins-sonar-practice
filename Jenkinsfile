pipeline {
    agent any

    tools {
        python 'Python 3'              // Jenkins Global Tools config me hona chahiye
        sonarScanner 'sonar-scanner'  // Yeh bhi Global Tools me hona chahiye
    }

    stages {
        stage('Checkout') {
            steps {
                git 'https://github.com/ERAPARH/Jenkins-sonar-practice' // ya local repo
            }
        }

        stage('Install Dependencies') {
            steps {
                sh 'pip install -r requirements.txt || true'  // agar koi req file hai
            }
        }

        stage('Run Tests') {
            steps {
                sh 'python3 -m unittest discover -s .'
            }
        }

        stage('SonarQube Analysis') {
            steps {
                withSonarQubeEnv('My SonarQube Server') {
                    sh 'sonar-scanner'
                }
            }
        }
    }
}
