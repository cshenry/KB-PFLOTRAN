/*
@author chenry kchen
*/
module KBaseReactiveTransport {
    typedef int bool;
    
    typedef string kbid;
    /*
		Reference to a file in KBase
    	@id handle
	*/
	typedef string handle_ref;
    
    /* 
    	PFlotranModel object
    	
    	@metadata ws name as Name
    	@metadata ws description as Description
		@optional hdf_parameters adjustable_parameters
    */
    typedef structure {
		string name;
		string description;
		list<tuple<string name,string type> > adjustable_parameters;
		handle_ref pflotran_deck;
		handle_ref hdf_parameters;
    } PflotranModel;
};
