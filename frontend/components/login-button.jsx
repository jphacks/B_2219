import { useSession, signIn, signOut } from "next-auth/react";

const LoginButton = () => {
  const { data: session } = useSession();

  if (!session) {
    return (<button onClick={() => signIn("github")}>Login with GitHub</button>);
  }

  return (<button onClick={() => signOut()}>Logout</button>);
};

export default LoginButton;
