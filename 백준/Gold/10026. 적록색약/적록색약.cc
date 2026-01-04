#include <iostream>
#include <queue>
#include <cstring>

using namespace std;
int N, cnt;
char map[102][102];
int dist[102][102];
bool visited[102][102];
int dir[4][2] = {{-1,0}, {1,0}, {0,-1}, {0,1}};


int bfs(int y, int x) {
    cnt++;
    queue<pair<int, int> > q;
    q.push(make_pair(y, x));
    visited[y][x] = true;

    int yc, xc, ya, xa, yn, xn;
    while(!q.empty()) {
        yc = q.front().first;
        xc = q.front().second;
        q.pop();

        for (int i = 0; i < 4; i++) {
            ya = yc + dir[i][0];
            xa = xc + dir[i][1];
            
            if((ya >= 0 && ya < N) && (xa >= 0 && xa < N) && !visited[ya][xa]) {
                if(map[ya][xa] == map[yc][xc]) {
                    visited[ya][xa] = true;
                    q.push(make_pair(ya, xa));
                    
                }
            }
        }
    }

    for (int i = 0; i < N; i++) {
        for (int j = 0; j < N; j++) {
            if(!visited[i][j]) {
               bfs(i, j);
            }
        }
    }

    return cnt;
}

int bfsColor(int y, int x) {
    cnt++;
    queue<pair<int, int> > q;
    q.push(make_pair(y, x));
    visited[y][x] = true;

    int yc, xc, ya, xa, yn, xn;
    while(!q.empty()) {
        yc = q.front().first;
        xc = q.front().second;
        q.pop();

        for (int i = 0; i < 4; i++) {
            ya = yc + dir[i][0];
            xa = xc + dir[i][1];
            
            if((ya >= 0 && ya < N) && (xa >= 0 && xa < N) && !visited[ya][xa]) {
                if(map[ya][xa] == map[yc][xc] || (map[ya][xa] == 'R' && map[yc][xc] == 'G') || (map[ya][xa] == 'G' && map[yc][xc] == 'R')) {
                    visited[ya][xa] = true;
                    q.push(make_pair(ya, xa));
                    
                }
            }
        }
    }

    for (int i = 0; i < N; i++) {
        for (int j = 0; j < N; j++) {
            if(!visited[i][j]) {
          
               bfsColor(i, j);
            }
        }
    }
    return cnt;
}

int main() {
    cin >> N;
    for (int i = 0; i < N; i++) {
        string s;
        cin >> s;
        for (int j = 0; j < N; j++) {
            map[i][j] = s[j];
        }
    }
    
    cout << bfs(0, 0) << ' ';
    memset(visited, false, sizeof(visited));
    cnt = 0;
    cout << bfsColor(0, 0);
    
}