import styles from "./repo_form.module.css";

const RepoForm = () => {
  const submitRepositoryForm = async (event) => {
    event.preventDefault();

    const repoRegex = /https:\/\/github.com\/(\w+)\/(\w+)/;
    const repoInfo = event.target.repo_url.value.match(repoRegex);
    if (repoInfo === null) {
      window.alert("GitHubリポジトリのURLを入力してください");
      return;
    }

    const response = await fetch("/projects", {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({
        "repository": {
          "owner": repoInfo[1],
          "name": repoInfo[2],
        }
      })
    });
  };

  return (
    <form method="POST" action="/api/projects" className={styles.repo_form}>
      <label htmlFor="repo_url">Repository URL</label>
      <input type="text" name="repo_url" id="repo_url" pattern="https:\/\/github.com\/\w+\/\w+" placeholder="https://github.com/username/repository" />
      <button type="submit">写経する</button>
    </form>
  );
};

export default RepoForm;
