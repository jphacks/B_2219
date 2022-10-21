import { unstable_getServerSession } from "next-auth/next"
import { authOptions } from "./auth/[...nextauth]"

const handler = async (req, res) => {
  if (req.method !== 'POST') {
    return res.redirect(302, `/?error_msg=unknown`);
  }
  const session = await unstable_getServerSession(req, res, authOptions);
  if (!session) {
    return res.status(400);
  }

  const repoRegex = /https:\/\/github.com\/(\w+)\/(\w+)/;
  const repoInfo = req.body.repo_url.match(repoRegex);
  if (repoInfo === null) {
    return res.redirect(302, `/?error_msg=unknown`);
  }

  const repoData = {
    "repository_owner": repoInfo[1],
    "repository_name": repoInfo[2],
    "creator_github_id": Number(session.user.id),
  };

  await fetch(`https://b-2219.fly.dev/projects/`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify(repoData),
  }).then((apiRes) => {
    return apiRes.json();
  }).then((apiResJSON) => {
    if (!apiResJSON.id) {
      switch (apiResJSON.detail) {
        case "Duplicate project":
          return res.redirect(302, `/?error_msg=duplicate_project`);
        default:
          throw new Error("API ERROR");
      }
    }
    return res.redirect(303, `/projects/${apiResJSON.id}`);
  }).catch((err) => {
    return res.redirect(302, `/?error_msg=unknown`);
  });
};

export default handler;
