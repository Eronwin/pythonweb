#include <string>
#include <vector>
#include <fnmatch.h>
using namespace std;

vector<string> vector_int2str(vector<int> input)
{
    vector<string> result;
    for (vector<int>::const_iterator it = input.begin();
         it != input.end();
         ++it)
    {
        result.push_back(to_string(*it));
    }
    return result;
}
vector<string> match(string origin, vector<string> pattern)
{
    vector<string> result;
    for (vector<string>::const_iterator it = pattern.begin();
         it != pattern.end();
         ++it)
    {
        if (fnmatch(it->c_str(), origin.c_str(), FNM_PATHNAME) == 0)
        {
            result.push_back(*it);
            printf("match: %s\n", it->c_str());
        }
        else
            printf("unmatch: %s\n", it->c_str());
    }
    return result;
}