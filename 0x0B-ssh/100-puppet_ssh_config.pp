#!/usr/bin/puppet
# configures ssh with puppet

 class { '::ssh::server':
    options => {
      'IdentityFile'             =>  '~/.ssh/holberton',
      'PasswordAuthentication'   => 'no',
    },
  }
