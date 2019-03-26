pipeline {
    agent any
    stages {
        stage('Build') {
            steps {
                echo "python build"
                sh 'python --version'

                sh 'python -m pip install -r requirements.txt'
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
               echo "python deploy"
               sh 'python app.py'
            }
        }
    }
}
