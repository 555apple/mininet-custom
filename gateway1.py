"""Custom topology example

Two directly connected switches plus a host for each switch:

   host --- host --- host

 sudo mn --custom ~/mininet/custom/gateway1.py --topo mytopo --pre ~/mininet/custom/gateway1_ip_conf

Adding the 'topos' dict with a key/value pair to generate our newly defined
topology enables one to pass in '--topo=mytopo' from the command line.
"""

from mininet.topo import Topo

class MyTopo( Topo ):
    "Simple topology example."

    def __init__( self ):
        "Create custom topo."

        # Initialize topology
        Topo.__init__( self )

        # Add hosts and switches
        host1 = self.addHost( 'h1' )
        host2 = self.addHost( 'h2' )
        host3 = self.addHost( 'h3' )
 	host4 = self.addHost( 'h4' )
	host5 = self.addHost( 'h5' )
	host6 = self.addHost( 'h6' )
	host7 = self.addHost( 'h7' )
	host8 = self.addHost( 'h8' )
	host9 = self.addHost( 'h9' )  
	host10 = self.addHost( 'h10' )       
	host11 = self.addHost( 'ser1' ) 

        # Add links
        self.addLink( host1, host2, port1=0,port2=0 )
        self.addLink( host2, host3, port1=1,port2=0 )
	self.addLink( host3, host4, port1=1,port2=0 )
        self.addLink( host4, host5, port1=1,port2=0 )
        self.addLink( host6, host2, port1=0,port2=2 )
	self.addLink( host7, host2, port1=0,port2=3 )
	self.addLink( host8, host2, port1=0,port2=4 )
	self.addLink( host9, host2, port1=0,port2=5 )
	self.addLink( host2, host10, port1=6,port2=0)
	self.addLink( host10, host4, port1=1,port2=2)
	self.addLink( host5, host11, port1=1,port2=0 )


topos = { 'mytopo': ( lambda: MyTopo() ) }
