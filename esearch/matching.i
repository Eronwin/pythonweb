%module matching 

%include "std_vector.i"
%include "std_string.i"





%{
    %include "matching.h"
    using namespace std;

    void test_str_list(vector<string> input);
%}

namespace std {
  %template(StringVector) vector<string>;
  %template(IntVector) vector<int>;
}

%include "matching.h"
using namespace std;
void test_str_list(vector<string> input);