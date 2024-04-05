[Go to README](README.md)

| Testcase | Expected Result | Test Result |
| -------- | --------------- | ----------- |
| **Profiles** | | | |
| _[Profile List](https://only-cute-api-2dbb94224813.herokuapp.com/profiles/)_ | | |
| GET Unauthenticated | returns 200 response: a list of all the profiles | PASS |
| GET Authenticated | returns 200 response: a list of all the profiles | PASS |
| POST, PUT, DELETE | Not provided | PASS |
| _[Profile Detail](https://only-cute-api-2dbb94224813.herokuapp.com/profiles/1)_ | | |
| GET Unauthenticated | returns 200 response: the profile specified by id | PASS |
| GET Authenticated | returns 200 response: the profile specified by id | PASS |
| POST, PUT, DELETE | Not provided | PASS |
| **Posts** | | |
| _[Posts List](https://only-cute-api-2dbb94224813.herokuapp.com/posts/)_ | | |
| GET Unauthenticated | returns 200 response: returns a list of all the posts | PASS |
| GET Authenticated | returns 200 response: returns a list of all the posts |PASS |
| POST Authenticated | returns 201 response: allows authenticated users to create posts | PASS |
| POST Unauthenticated | returns 403 error | PASS |
| PUT, DELETE | Not provided | PASS |
| _[Post Detail](https://only-cute-api-2dbb94224813.herokuapp.com/posts/3)_ | | |
| GET Unauthenticated | returns the post specified by id | PASS |
| GET Authenticated Owner | returns the post specified by id | PASS |
| GET Authenticated Not Owner | returns the post specified by id without put form | PASS |
| PUT Authenticated Owner | allows the owner to update the post | PASS |
| PUT Authenticated Not Owner | returns 403 error | PASS |
| PUT Unauthenticated | returns 403 error | PASS |
| DELETE Authenticated Owner | returns 204 response: post is deleted | PASS |
| DELETE Authenticated Not Owner | returns 403 error | PASS |
| DELETE Unauthenticated | returns 403 error | PASS |
| POST | Not provided | PASS |
| **Comments** | | |
| _[Comments List](https://only-cute-api-2dbb94224813.herokuapp.com/comments/)_ | | |
| GET Unauthenticated | returns a list of all the comments from a specified post | PASS |
| GET Authenticated | returns a list of all the comments from a specified post | PASS |
| POST Authenticated | returns 201 response: allows authenticated users to create comments | PASS |
| POST Authenticated | returns 403 error | PASS |
| PUT, DELETE | Not provided | PASS |  |
| _[Comment Detail](https://only-cute-api-2dbb94224813.herokuapp.com/comments/3)_ | | |
| GET Unauthenticated | returns the comment specified by id | PASS |
| GET Authenticated | returns the comment specified by id | PASS |
| PUT Authenticated Owner | allows the owner to update the comment | PASS |
| PUT Authenticated Not Owner | returns 403 error | PASS |
| PUT Unauthenticated | returns 403 error | PASS |
| DELETE Authenticated Owner | returns 204 response, comment is deleted | PASS |
| DELETE Authenticated Not Owner | returns 403 error | PASS |
| DELETE Unauthenticated | returns 403 error | PASS |
| POST | Not Provided | Pass |
| **Followers** | | |
| _[Followers List](https://only-cute-api-2dbb94224813.herokuapp.com/followers/)_ | | |
| GET Unauthenticated | returns 200 response: a list of all the followers | PASS |
| GET Authenticated | returns 200 response: a list of all the followers | PASS |
| POST, PUT, DELETE | Not provided | PASS |
| _[Follower Detail](https://only-cute-api-2dbb94224813.herokuapp.com/followers/5/)_ | | |
| GET Unauthenticated | returns 200 response: the follower specified by id | PASS |
| GET Authenticated | returns 200 response: the follower specified by id | PASS |
| POST Authenticated | returns 201 response: allows authenticated users to follow a user | PASS |
| POST Unauthenticated | returns 403 error | PASS |
| PUT, DELETE | Not provided | PASS |
| **Likes** | | |
| _[Likes List](https://only-cute-api-2dbb94224813.herokuapp.com/likes/)_ | | |
| GET Unauthenticated | returns 200 response: a list of all the likes | PASS |
| GET Authenticated | returns 200 response: a list of all the likes | PASS |
| POST, PUT, DELETE | Not provided | PASS |
| _[Liked Detail](https://only-cute-api-2dbb94224813.herokuapp.com/likes/2)_ | | |
| GET Unauthenticated | returns 200 response: the like specified by id | PASS |
| GET Authenticated | returns 200 response: the like specified by id | PASS |
| POST Authenticated | returns 201 response: allows authenticated users to like a post | PASS |
| POST Unauthenticated | returns 403 error | PASS |
| PUT, DELETE | Not provided | PASS |
| **Saved Posts** | | |
| _[Saved Posts List](https://only-cute-api-2dbb94224813.herokuapp.com/saved_posts/)_ | | |
| GET Unauthenticated | returns 200 response: a list of all the saved posts | PASS |
| GET Authenticated | returns 200 response: a list of all the saved posts | PASS |
| POST, PUT, DELETE | Not provided | PASS |
| _[Saved Post Detail](https://only-cute-api-2dbb94224813.herokuapp.com/saved_posts/2)_ | | |
| GET Unauthenticated | returns 200 response: the saved_post specified by id | PASS |
| GET Authenticated | returns 200 response: the saved_post specified by id | PASS |
| POST Authenticated | returns 201 response: allows authenticated users to save a post | PASS |
| POST Unauthenticated | returns 403 error | PASS |
| PUT, DELETE | Not provided | PASS |
