pipeline {
    agent any
    stages {
        stage('Preparation environment') {
            steps {
                dir('HW_2') {
                    sh 'python3 data_preprocessing.py'
                }
            }
        }
        stage('Model training') {
            steps {
                dir('HW_2') {
                    sh 'python3 model_preparation.py'
                }
            }
        }
        stage('Model testing') {
            steps {
                dir('HW_2') {
                    sh 'python3 model_testing.py'
                }
            }
        }
    }
    post {
        always {
            echo 'The pipeline is finished!'
        }
        success {
            echo 'The build was successful!'
        }
        failure {
            echo 'The build failed.'
        }
    }
}
