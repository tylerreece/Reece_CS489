# primarysecondaryclassifier

Instructions for running:

	(1) pcap (see 2013-10-21_capture-1-only-dns.pcap as example
	(2) utilize TShark to get dns query names 
		tshark -r <yourpcap.pcap> -T fields -e dns.qry.name > <textfile.txt>
	(3) run featureExtractor to get csv of feature fields from text file
		python dnsFeatureExtractor.py <textfile.txt> <output.csv>
	(4) run kneighbors.py to create and test model
		python kneighbors.py <k_value> <input.csv>
		
		