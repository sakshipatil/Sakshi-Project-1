pipeline {
    agent any
    stages {
        stage('Build') {
            steps {
                echo '$PATH'
                echo 'Hello ..'

                bat 'python --version'
                bat 'ipconfig'
                bat 'python -m pip install -r Requirements.txt'
                echo 'Building..'

            }
        }
        stage('Test') {
            steps {
                echo 'Testing..'
                bat 'python app.py'
            }
        }
        stage('Deploy') {
            steps {
                echo 'Deploying....'
                bat 'python app.py'
            }
        }
    }
}