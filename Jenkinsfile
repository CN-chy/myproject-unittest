pipeline {
  agent {
    node {
      label 'test'
    }
  }
    stages {
        stage('checkout') {
            steps {
                git credentialsId: 'd6deccd5-684f-4745-886f-939874d54721', url: 'https://github.com/CN-chy/myproject-unittest.git'
            }
        }
        stage('DataConfig') {
            steps {
                echo 'DataConfig'
            }
        }
        stage('user') {
            steps {
            bat '''python unit/security/security.py'''
            }
        }
        stage('order') {
            steps {
            bat '''python unit/order/order.py'''
            }
        }
        stage('payment') {
            steps {
            bat '''python unit/payment/payment.py'''
            }
        }
        stage('security') {
            steps {
            bat '''python unit/security/security.py'''
            }
        }
    }
}
