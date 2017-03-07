"""Custom topology example

Two directly connected switches plus a host for each switch:

   host --- host --- host 三台主机都接在同一个交换机上

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
	s1=self.addSwitch('s1')
	
       
        # Add links
        self.addLink( host1, s1 )
        self.addLink( host2, s1 )
        self.addLink( host3, s1 )
 


      


topos = { 'mytopo': ( lambda: MyTopo() ) }
