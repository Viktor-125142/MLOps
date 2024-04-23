pipeline {
    agent any
    stages {
        stage('Setup virtual environment') {
            steps {
                dir('HW_2') {
                    sh 'python3 -m venv env'
                }
            }
        }
        stage('Preparation environment') {
            steps {
                dir('HW_2') {
                    sh '''
                    source env/bin/activate
                    pip install -r requirements.txt
                    python3 data_preprocessing.py
                    '''
                }
            }
        }
        stage('Model training') {
            steps {
                dir('HW_2') {
                    sh '''
                    source env/bin/activate
                    python3 model_preparation.py
                    '''
                }
            }
        }
        stage('Model testing') {
            steps {
                dir('HW_2') {
                    sh '''
                    source env/bin/activate
                    $(pwd)/python3 model_testing.py
                    '''
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
