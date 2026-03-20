pipeline {
    agent any

    stages {
        stage('Clone') {
            steps {
                git 'https://github.com/Gallagowtham/dockerwithpytest.git'
            }
        }
        stage('Build') {
            steps {
                sh 'docker build -t gowthagalla/seleniumwithdocker .'
            }
        }
        stage('Test') {
            steps {
                sh 'docker run gowthagalla/seleniumwithdocker'
            }
        }
        stage('Push') {
            steps {
                sh 'docker push gowthagalla/seleniumwithdocker'
            }
        }
    }

    post {
        success {
            echo 'Pipeline SUCCESS!'
        }
        failure {
            echo 'Pipeline FAILED!'
        }
    }
}