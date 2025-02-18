pipeline {
  agent {
    node {
      label 'test'
    }
  }
    stages {
        stage('checkout') {
            steps {
            git branch: master, credentialsId: 'efde19be-c1ba-4360-8a09-514fe653079e', url: 'https://github.com/CN-chy/position.git'
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
