
auto get_exchange(auto ampo) {
    ifstream jfile; // file to read
    jfile.open("couplings.in"); // file with the coupling
    int nj;
    jfile >> nj; // read the number of couplings
    float jxx[nj]; // declare js
    float jxy[nj]; // declare js
    float jxz[nj]; // declare js
    float jyx[nj]; // declare js
    float jyy[nj]; // declare js
    float jyz[nj]; // declare js
    float jzx[nj]; // declare js
    float jzy[nj]; // declare js
    float jzz[nj]; // declare js
    int indexj1[nj]; // declare index
    int indexj2[nj]; // declare index
    for (int i=0;i<nj;++i) {
//      cout << i << endl ;
      jfile >> indexj1[i] >> indexj2[i] >>
      jxx[i] >> jxy[i] >> jxz[i] >> // read this coupling
      jyx[i] >> jyy[i] >> jyz[i] >> // read this coupling
      jzx[i] >> jzy[i] >> jzz[i] ; // read this coupling
    } ;
    jfile.close() ;


    int j1,j2; // indexes
    float jc ; // value
    for(int j=0; j < nj; ++j)
        {
        j1 = indexj1[j]+1;
        j2 = indexj2[j]+1;
        ampo += jxx[j],"Sx",j1,"Sx",j2;
        ampo += jxy[j],"Sx",j1,"Sy",j2;
        ampo += jxz[j],"Sx",j1,"Sz",j2;
        ampo += jyx[j],"Sy",j1,"Sx",j2;
        ampo += jyy[j],"Sy",j1,"Sy",j2;
        ampo += jyz[j],"Sy",j1,"Sz",j2;
        ampo += jzx[j],"Sz",j1,"Sx",j2;
        ampo += jzy[j],"Sz",j1,"Sy",j2;
        ampo += jzz[j],"Sz",j1,"Sz",j2;
        }
    return ampo ;  // return the Hamiltonian with exchange added
}
