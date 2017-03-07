"""Custom topology example

Two directly connected switches plus a host for each switch:

   host --- switch --- switch --- host

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
	
        # Add nodes for domain 1
	d1rm   = self.addHost( 'd1rm' )
        d1pub1 = self.addHost( 'd1pub1' )
        d1sub1 = self.addHost( 'd1sub1' )
        d1br1  = self.addHost( 'd1br1' )

	s1 = self.addSwitch( 's1' )

        # Add links for domain 1
        self.addLink( d1rm     , s1, port1=1,port2=1 )
        self.addLink( d1sub1   , s1, port1=1,port2=2 )
        self.addLink( d1pub1   , s1, port1=1,port2=3 )
        self.addLink( d1br1    , s1, port1=2,port2=4 )

        # Add nodes for domain 2
	d2rm   = self.addHost( 'd2rm' )
        d2pub1 = self.addHost( 'd2pub1' )
        d2sub1 = self.addHost( 'd2sub1' )
        d2br1  = self.addHost( 'd2br1' )

	s2 = self.addSwitch( 's2' )

        # Add links for domain 2
        self.addLink( d2rm     , s2, port1=1,port2=1 )
        self.addLink( d2sub1   , s2, port1=1,port2=2 )
        self.addLink( d2pub1   , s2, port1=1,port2=3 )
        self.addLink( d2br1    , s2, port1=2,port2=4 )

        # Add nodes for domain 3
	d3rm   = self.addHost( 'd3rm' )
        d3pub1 = self.addHost( 'd3pub1' )
        d3sub1 = self.addHost( 'd3sub1' )
        d3br1  = self.addHost( 'd3br1' )
        d3br2  = self.addHost( 'd3br2' )
        d3br3  = self.addHost( 'd3br3' )

	s3 = self.addSwitch( 's3' )

        # Add links for domain 3
        self.addLink( d3rm     , s3, port1=1,port2=1 )
        self.addLink( d3sub1   , s3, port1=1,port2=2 )
        self.addLink( d3pub1   , s3, port1=1,port2=3 )
        self.addLink( d3br1    , s3, port1=2,port2=4 )
        self.addLink( d3br2    , s3, port1=2,port2=5 )
        self.addLink( d3br3    , s3, port1=2,port2=6 )

        # Add nodes for domain 4
	d4rm   = self.addHost( 'd4rm' )
        d4pub1 = self.addHost( 'd4pub1' )
        d4sub1 = self.addHost( 'd4sub1' )
        d4br1  = self.addHost( 'd4br1' )

	s4 = self.addSwitch( 's4' )

        # Add links for domain 4
        self.addLink( d4rm     , s4, port1=1,port2=1 )
        self.addLink( d4sub1   , s4, port1=1,port2=2 )
        self.addLink( d4pub1   , s4, port1=1,port2=3 )
        self.addLink( d4br1    , s4, port1=2,port2=4 )

        # Add nodes for domain 5
	d5rm   = self.addHost( 'd5rm' )
        d5pub1 = self.addHost( 'd5pub1' )
        d5sub1 = self.addHost( 'd5sub1' )
        d5cr2  = self.addHost( 'd5cr2' )
        d5br1  = self.addHost( 'd5br1' )
        d5br2  = self.addHost( 'd5br2' )
        d5br3  = self.addHost( 'd5br3' )

	s5 = self.addSwitch( 's5' )

        # Add links for domain 5
        self.addLink( s5       , d5cr2, port1=1,port2=1 )
        self.addLink( d5rm     , d5cr2, port1=1,port2=2 )
        self.addLink( d5sub1   , s5, port1=1,port2=2 )
        self.addLink( d5pub1   , d5cr2, port1=1,port2=3 )
        self.addLink( d5br1    , s5, port1=2,port2=3 )
        self.addLink( d5br3    , s5, port1=2,port2=4 )
        self.addLink( d5br2    , d5cr2, port1=2,port2=4 )

        # Add nodes for domain 6
	d6rm   = self.addHost( 'd6rm' )
        d6pub1 = self.addHost( 'd6pub1' )
        d6sub1 = self.addHost( 'd6sub1' )
        d6br1  = self.addHost( 'd6br1' )
        d6br2  = self.addHost( 'd6br2' )

	s6 = self.addSwitch( 's6' )

        # Add links for domain 6
        self.addLink( d6rm     , s6, port1=1,port2=1 )
        self.addLink( d6sub1   , s6, port1=1,port2=2 )
        self.addLink( d6pub1   , s6, port1=1,port2=3 )
        self.addLink( d6br1    , s6, port1=2,port2=4 )
        self.addLink( d6br2    , s6, port1=3,port2=5 )

        # Add nodes for inter domain path
	s13 = self.addSwitch( 's13' )
	s23 = self.addSwitch( 's23' )
	s36 = self.addSwitch( 's36' )
	s45 = self.addSwitch( 's45' )
	s56 = self.addSwitch( 's56' )

        # Add links for inter domain path
        #self.addLink( d1br1     , s13, port1=1,port2=1 )
        #self.addLink( d3br2     , s13, port1=1,port2=2 )
        #self.addLink( d2br1     , s23, port1=1,port2=1 )
        #self.addLink( d3br3     , s23, port1=1,port2=2 )
        #self.addLink( d4br1     , s45, port1=1,port2=1 )
        #self.addLink( d5br3     , s45, port1=1,port2=2 )
        #self.addLink( d3br1     , s36, port1=1,port2=1 )
        #self.addLink( d6br1     , s36, port1=1,port2=2 )
        #self.addLink( d5br1     , s56, port1=1,port2=1 )
        #self.addLink( d6br2     , s56, port1=1,port2=2 )
        #self.addLink( d5br2     , s56, port1=1,port2=3 )
        #self.addLink( d6br2     , s56, port1=2,port2=4 )


topos = { 'mytopo': ( lambda: MyTopo() ) }
