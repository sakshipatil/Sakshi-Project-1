pipeline {
    agent any
    stages {
        stage('Build') {
            steps {
                echo "python bulid"
                bat 'python --version'

                bat 'python -m pip install -r requirements.txt'
                echo 'Building..'
            }
        }
        stage('Test') {
            steps {
                echo "python test"
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
