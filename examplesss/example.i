%module example

%include "std_string.i"
%include "std_vector.i"

%{
using namespace std;

vector<string> vector_int2str(vector<int> input);
vector<string> match(string origin, vector<string> pattern);
%}

namespace std {
  %template(StringVector) vector<string>;
  %template(IntVector) vector<int>;
}

using namespace std;

vector<string> vector_int2str(vector<int> input);
vector<string> match(string origin, vector<string> pattern);