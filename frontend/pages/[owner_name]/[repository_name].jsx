import { useRouter } from "next/router";

import Editor, { DiffEditor, useMonaco, loader } from "@monaco-editor/react";

import Header from "../../components/header";
import Layout from "../../components/layout";

const ShakyoPage = () => {
  const router = useRouter();

  const { owner_name, repository_name } = router.query;

  return (
    <Layout>
      <Header />
      <DiffEditor
        height="calc(100vh - 1rem)"
        theme="vs-dark"
        original={`THIS IS TEST ${owner_name}`}
        modified={`THIS IS TEST ${repository_name}`}
        options={
          {
            minimap: { enabled: false },
          }
        }
      />
    </Layout>
  );
};

export default ShakyoPage;
