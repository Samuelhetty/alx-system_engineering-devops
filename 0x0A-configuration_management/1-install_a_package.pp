# Using Puppet, install flask from pip3.

# Requirements:

# Installs flask
# Version must be 2.1.0

Package { 'python3.8':
    ensure => '3.8.10',
}

Package { 'python3-pip':
    ensure => installed,
}

package { 'flask':
    ensure   => '2.1.0',
    require  => Package['python3-pip'],
    provider => 'pip',
}

package { 'Werkzeug':
    ensure   => '2.2.2',
    require  => Package['python3-pip'],
    provider => 'pip',
}
