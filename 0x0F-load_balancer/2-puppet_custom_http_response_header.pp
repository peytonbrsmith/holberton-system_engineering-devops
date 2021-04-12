#!/usr/bin/puppet
# configures nginx

package { 'nginx':
  ensure => installed,
}

file_line { 'newheader':
  ensure => 'present',
  path   => '/etc/nginx/sites-available/default',
  after  => 'server_name _;',
  line   => 'add_header X-Served-By \$HOSTNAME;',
}

service { 'nginx':
  ensure  => running,
  restart => true,
  require => Package['nginx'],
}
