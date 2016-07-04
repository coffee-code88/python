Vagrant.configure(2) do |config|
  config.vm.box = "ubuntu/trusty64"
  config.vm.hostname = "coding-server"
  config.vm.network "private_network", ip: "192.168.99.200"

  config.vm.provider "virtualbox" do |vb|
    vb.gui = false
    vb.memory = 1024
    vb.cpus = 1
  end
  config.vm.provision "shell", inline: <<-SHELL
     sudo apt-get update
     sudo apt-get install -y whois git
     sudo useradd -m -p `mkpasswd password` -s /bin/bash dev
     sudo usermod -a -G sudo dev
  SHELL
end
