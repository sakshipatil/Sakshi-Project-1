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
            }
        }
        stage('Deploy') {
            steps {
               sh "python deploy"
            }
        }
    }
}