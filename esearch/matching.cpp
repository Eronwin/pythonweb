#include "matching.h"
using namespace std;
void Matching::el_search()
{
    const char *orgin_str = "sina|weibo|pusher";
    char pattern_arr[][20] = {
        {"sina|*|pusher"},
        {"sina|*|*"},
        {"*|weibo|*"},
        //不能被匹配的
        {"sina|pic|*"},
        {"*|*|sign"},
        {"*|weibo|sign"},
        {"*|pic|sign"},
        {"sina|pic|sign"},

        {"*|*|*"}};
    static int pattern_arr_size = sizeof(pattern_arr) / sizeof(pattern_arr[0]);

    vector<char *> vec_str;
    for (int i = 0; i < pattern_arr_size; i++)
    {
        vec_str.push_back(pattern_arr[i]);
    }

    std::cout << "Origin Str: " << orgin_str << "\n\n";
    int ret;
    for (int i = 0; i < vec_str.size(); i++)
    {
        ret = fnmatch(vec_str.at(i), orgin_str, FNM_PATHNAME);
        if (ret == FNM_NOMATCH)
        {
            cout << "sorry, I'm failed: [" << vec_str.at(i) << "]\n";
        }
        else
        {
            cout << "OK, I'm success: [" << vec_str.at(i) << "]\n";
        }
    }
}

void Matching::test_str_list(vector<string> ff)
{
    for (vector<string>::iterator it = ff.begin(); it != ff.end(); it++)
    {
        cout << *it << endl;
    }
}