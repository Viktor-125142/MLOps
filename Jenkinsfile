pipeline {
    agent any
    stages {
        stage('Setup virtual environment') {
            steps {
                dir('HW_2') {
                    // Создание виртуальной среды только один раз
                    sh 'python3 -m venv env'
                }
            }
        }
        stage('Preparation environment') {
            steps {
                dir('HW_2') {
                    // Активация виртуальной среды и установка зависимостей на каждой стадии
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
                    // Повторно активировать виртуальную среду для следующей стадии
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
                    // И снова активация виртуальной среды для этой стадии
                    sh '''
                    source env/bin/activate
                    python3 model_testing.py
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
