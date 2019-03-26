pipeline {
    agent any
    stages {
        stage('Build') {
            steps {
                sh "python bulid"

            }
        }
        stage('Test') {
            steps {
                sh "python test"
                bat 'python app.py'
            }
        }
        stage('Deploy') {
            steps {
               sh "python deploy"
               bat 'python app.py'
            }
        }
    }
}