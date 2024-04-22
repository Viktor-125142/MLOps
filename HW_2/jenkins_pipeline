pipeline {
    agent any

    stages {
        stage('Preparation environment') {
            steps {
                sh 'python3 data_preprocessing.py'
            }
        }
        stage('Model training') {
            steps {
                sh 'python3 model_preparation.py'
            }
        }
        stage('Model testing') {
            steps {
                sh 'python3 model_testing.py'
            }
        }
    }
    post {
        always {
            // Здесь вы можете добавить шаги, которые выполнятся после завершения сборки
            echo 'The pipeline is finished!'
        }
        success {
            // Действия, выполняемые только при успешной сборке
            echo 'The build was successful!'
        }
        failure {
            // Действия, выполняемые в случае неудачной сборки
            echo 'The build failed.'
        }
    }
}
