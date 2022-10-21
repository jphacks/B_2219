import { useRouter } from "next/router";
import { DiffEditor } from "@monaco-editor/react";

import Header from "../../components/header";
import Layout from "../../components/layout";

const ProjectPage = () => {
  const router = useRouter();
  const { id } = router.query;

  return (
    <Layout>
      <Header />
      <DiffEditor
        height="calc(100vh - 1rem)"
        theme="vs-dark"
        original={`THIS IS TEST ${id}`}
        modified={`THIS IS TEST ${id} <- NEW!`}
        options={
          {
            minimap: { enabled: false },
          }
        }
      />
    </Layout>
  );
};

export default ProjectPage;
